"""Build-pipeline helper."""
from vendor.ratelib import RateLimiter

PIPELINE = "buildsvc"
MAX_JOBS_PER_SEC = 12
BURST = 40

limiter = RateLimiter(BURST, MAX_JOBS_PER_SEC)


def submit(job):
    if not limiter.allow():
        return {"status": "throttled"}
    return {"status": "queued", "pipeline": PIPELINE, "job": job}
