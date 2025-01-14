<template>
    <div class="flip-card">
        <div class="flip-card-inner">
            <div class="flip-card-front">
                <h2>{{ front }}</h2>
            </div>
            <div class="flip-card-back">
                <h2>{{ back }}</h2>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'flashcard-component',
    props: ['front', 'back']
}
</script>

<style>
.flip-card {
    background-color: transparent;
    width: 300px;
    height: 300px;
    perspective: 1000px;
}

.flip-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    text-align: center;
    transition: transform 0.6s;
    transform-style: preserve-3d;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
}

.flip-card:hover .flip-card-inner {
    transform: rotateY(180deg);
}

.flip-card-front,
.flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    box-sizing: border-box;
    font-size: 38px;
    white-space: nowrap;
}

.flip-card-front {
    color: black;
    border: 10px solid black;
    border-style: dashed
}

.flip-card-back {
    transform: rotateY(180deg);
}
</style>