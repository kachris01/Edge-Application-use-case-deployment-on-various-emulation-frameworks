This is a demo app with exemplary fault tolerance features.

It consist of two instances of UDP servers (``temperature-server``),
which each reply with an artificial temperature value when receiving
the byte string ``temp``.

The second component is a voter (UDP client, ``temperature-voter``)
which frequently (~ 1 Hz) queries and prints temperature values from
two of the servers described above. Currently, the servers must be
available under the host names ``server_a`` and ``server_b``
(hardcoded). If both servers reply, the values are averaged.
