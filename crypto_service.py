"""crypto_service.py - the OUTSIDE COMPONENT.

A standalone module with no Flask code in it. It holds the security
functions that the web app calls.
"""
import hashlib
import secrets


def sha256_hash(text):
    """Return the SHA-256 fingerprint of a piece of text (integrity check)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def generate_hybrid_session_key():
    """SIMULATE hybrid key encapsulation (teaching demo, not real crypto).

    Real hybrid schemes combine a classical secret (e.g. X25519) with a
    post-quantum secret (e.g. Kyber/ML-KEM). Here both secrets are random
    bytes, and they are combined with SHA-256 into one session key. An
    attacker would need to break BOTH secrets to recover the key.
    """
    classical_secret = secrets.token_bytes(32)      # stands in for ECDH
    post_quantum_secret = secrets.token_bytes(32)   # stands in for Kyber
    session_key = hashlib.sha256(classical_secret + post_quantum_secret).hexdigest()
    return {
        "classical_secret": classical_secret.hex(),
        "post_quantum_secret": post_quantum_secret.hex(),
        "session_key": session_key,
    }
