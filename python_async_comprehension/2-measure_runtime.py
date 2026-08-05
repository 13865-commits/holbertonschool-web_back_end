#!/usr/bin/env python3
"""Measure Runtime module."""
import asyncio
git pushit -m "Fix python_async_comprehension tasks with correct AsyncGenerator type hints"
[main f4e0f3c] Fix python_async_comprehension tasks with correct AsyncGenerator type hints
 3 files changed, 32 insertions(+), 2 deletions(-)
 mode change 100644 => 100755 python_async_comprehension/0-async_generator.py
 create mode 100755 python_async_comprehension/1-async_comprehension.py
 create mode 100755 python_async_comprehension/2-measure_runtime.py
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 2 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 1010 bytes | 1010.00 KiB/s, done.
Total 6 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/13865-commits/holbertonschool-web_back_end.git
   cdd33ff..f4e0f3c  main -> main
root@dc84991026bd45c5ba5c16933937c73a-2377118072:~/holbertonschool-web_back_end# cd ~/holbertonschool-web_back_end
mkdir -p python_async_comprehension
cd python_async_comprehension

cat << 'EOF' > 0-async_generator.py
#!/usr/bin/env python3
"""
Module for async_generator coroutine.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that loops 10 times, asynchronously waits 1 second,
    and yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
