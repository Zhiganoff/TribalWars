#!/bin/bash
commands=(
    "sleep 2"
    "key Return"
    "sleep 0.1"
    "key Ctrl+Tab"
    "sleep 0.1"
    "key Return"
    "sleep 0.1"
    "key Ctrl+Tab"
    "sleep 0.1"
    "key Return"
    "sleep 0.1"
    "key Ctrl+Tab"
    "sleep 0.1"
    "key Return"
    "sleep 0.1"
    "key Ctrl+Tab"
    "sleep 0.1"
)
xdotool ${commands[*]}