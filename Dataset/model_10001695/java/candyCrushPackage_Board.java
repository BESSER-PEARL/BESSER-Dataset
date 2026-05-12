





import java.util.List;
import java.util.ArrayList;

public class candyCrushPackage_Board  {

    private String cascadeTimer;
    private int HORIZONTAL_GAP;
    private int baseScorePerCandy;
    private None selfCrushCandy;
    private int BOARD_HEIGHT;
    private int moveDistance;
    private int selfCrushTimerCount;
    private int BOARD_WIDTH;
    private String dropTimer;
    private String swapTimer;
    private int candyWidth;
    private int dropTimerCount;
    private int swapTimerCount;
    private String selfCrushTimer;
    private None swapDirection;
    private None secondPressedCandy;
    private int movesLeft;
    private int movesPerGame;
    private String crushTimer;
    private int candyHeight;
    private int gameScore;
    private int crushTimerCount;
    private int VERTICAL_GAP;
    private None firstPressedCandy;
    private int SIZE;
    private boolean isFirstPressed;
    private String scorePerCandy;
    private int delay;
    private boolean isSwapBack;





    private List<candyCrushPackage_Candy> candycrushpackage_candys;




    private candyCrushPackage_Game candycrushpackage_game;


    public candyCrushPackage_Board(
        String cascadeTimer,        int HORIZONTAL_GAP,        int baseScorePerCandy,        None selfCrushCandy,        int BOARD_HEIGHT,        int moveDistance,        int selfCrushTimerCount,        int BOARD_WIDTH,        String dropTimer,        String swapTimer,        int candyWidth,        int dropTimerCount,        int swapTimerCount,        String selfCrushTimer,        None swapDirection,        None secondPressedCandy,        int movesLeft,        int movesPerGame,        String crushTimer,        int candyHeight,        int gameScore,        int crushTimerCount,        int VERTICAL_GAP,        None firstPressedCandy,        int SIZE,        boolean isFirstPressed,        String scorePerCandy,        int delay,        boolean isSwapBack    ) {
        this.cascadeTimer = cascadeTimer;
        this.HORIZONTAL_GAP = HORIZONTAL_GAP;
        this.baseScorePerCandy = baseScorePerCandy;
        this.selfCrushCandy = selfCrushCandy;
        this.BOARD_HEIGHT = BOARD_HEIGHT;
        this.moveDistance = moveDistance;
        this.selfCrushTimerCount = selfCrushTimerCount;
        this.BOARD_WIDTH = BOARD_WIDTH;
        this.dropTimer = dropTimer;
        this.swapTimer = swapTimer;
        this.candyWidth = candyWidth;
        this.dropTimerCount = dropTimerCount;
        this.swapTimerCount = swapTimerCount;
        this.selfCrushTimer = selfCrushTimer;
        this.swapDirection = swapDirection;
        this.secondPressedCandy = secondPressedCandy;
        this.movesLeft = movesLeft;
        this.movesPerGame = movesPerGame;
        this.crushTimer = crushTimer;
        this.candyHeight = candyHeight;
        this.gameScore = gameScore;
        this.crushTimerCount = crushTimerCount;
        this.VERTICAL_GAP = VERTICAL_GAP;
        this.firstPressedCandy = firstPressedCandy;
        this.SIZE = SIZE;
        this.isFirstPressed = isFirstPressed;
        this.scorePerCandy = scorePerCandy;
        this.delay = delay;
        this.isSwapBack = isSwapBack;
        this.candycrushpackage_candys = new ArrayList<>();
    }

    public candyCrushPackage_Board(
        String cascadeTimer,        int HORIZONTAL_GAP,        int baseScorePerCandy,        None selfCrushCandy,        int BOARD_HEIGHT,        int moveDistance,        int selfCrushTimerCount,        int BOARD_WIDTH,        String dropTimer,        String swapTimer,        int candyWidth,        int dropTimerCount,        int swapTimerCount,        String selfCrushTimer,        None swapDirection,        None secondPressedCandy,        int movesLeft,        int movesPerGame,        String crushTimer,        int candyHeight,        int gameScore,        int crushTimerCount,        int VERTICAL_GAP,        None firstPressedCandy,        int SIZE,        boolean isFirstPressed,        String scorePerCandy,        int delay,        boolean isSwapBack        ArrayList<candyCrushPackage_Candy> candycrushpackage_candys    ) {
        this.cascadeTimer = cascadeTimer;
        this.HORIZONTAL_GAP = HORIZONTAL_GAP;
        this.baseScorePerCandy = baseScorePerCandy;
        this.selfCrushCandy = selfCrushCandy;
        this.BOARD_HEIGHT = BOARD_HEIGHT;
        this.moveDistance = moveDistance;
        this.selfCrushTimerCount = selfCrushTimerCount;
        this.BOARD_WIDTH = BOARD_WIDTH;
        this.dropTimer = dropTimer;
        this.swapTimer = swapTimer;
        this.candyWidth = candyWidth;
        this.dropTimerCount = dropTimerCount;
        this.swapTimerCount = swapTimerCount;
        this.selfCrushTimer = selfCrushTimer;
        this.swapDirection = swapDirection;
        this.secondPressedCandy = secondPressedCandy;
        this.movesLeft = movesLeft;
        this.movesPerGame = movesPerGame;
        this.crushTimer = crushTimer;
        this.candyHeight = candyHeight;
        this.gameScore = gameScore;
        this.crushTimerCount = crushTimerCount;
        this.VERTICAL_GAP = VERTICAL_GAP;
        this.firstPressedCandy = firstPressedCandy;
        this.SIZE = SIZE;
        this.isFirstPressed = isFirstPressed;
        this.scorePerCandy = scorePerCandy;
        this.delay = delay;
        this.isSwapBack = isSwapBack;
        this.candycrushpackage_candys = candycrushpackage_candys;
    }

    public String getCascadetimer() {
        return cascadeTimer;
    }

    public void setCascadetimer(String cascadeTimer) {
        this.cascadeTimer = cascadeTimer;
    }
    public int getHorizontal_gap() {
        return HORIZONTAL_GAP;
    }

    public void setHorizontal_gap(int HORIZONTAL_GAP) {
        this.HORIZONTAL_GAP = HORIZONTAL_GAP;
    }
    public int getBasescorepercandy() {
        return baseScorePerCandy;
    }

    public void setBasescorepercandy(int baseScorePerCandy) {
        this.baseScorePerCandy = baseScorePerCandy;
    }
    public None getSelfcrushcandy() {
        return selfCrushCandy;
    }

    public void setSelfcrushcandy(None selfCrushCandy) {
        this.selfCrushCandy = selfCrushCandy;
    }
    public int getBoard_height() {
        return BOARD_HEIGHT;
    }

    public void setBoard_height(int BOARD_HEIGHT) {
        this.BOARD_HEIGHT = BOARD_HEIGHT;
    }
    public int getMovedistance() {
        return moveDistance;
    }

    public void setMovedistance(int moveDistance) {
        this.moveDistance = moveDistance;
    }
    public int getSelfcrushtimercount() {
        return selfCrushTimerCount;
    }

    public void setSelfcrushtimercount(int selfCrushTimerCount) {
        this.selfCrushTimerCount = selfCrushTimerCount;
    }
    public int getBoard_width() {
        return BOARD_WIDTH;
    }

    public void setBoard_width(int BOARD_WIDTH) {
        this.BOARD_WIDTH = BOARD_WIDTH;
    }
    public String getDroptimer() {
        return dropTimer;
    }

    public void setDroptimer(String dropTimer) {
        this.dropTimer = dropTimer;
    }
    public String getSwaptimer() {
        return swapTimer;
    }

    public void setSwaptimer(String swapTimer) {
        this.swapTimer = swapTimer;
    }
    public int getCandywidth() {
        return candyWidth;
    }

    public void setCandywidth(int candyWidth) {
        this.candyWidth = candyWidth;
    }
    public int getDroptimercount() {
        return dropTimerCount;
    }

    public void setDroptimercount(int dropTimerCount) {
        this.dropTimerCount = dropTimerCount;
    }
    public int getSwaptimercount() {
        return swapTimerCount;
    }

    public void setSwaptimercount(int swapTimerCount) {
        this.swapTimerCount = swapTimerCount;
    }
    public String getSelfcrushtimer() {
        return selfCrushTimer;
    }

    public void setSelfcrushtimer(String selfCrushTimer) {
        this.selfCrushTimer = selfCrushTimer;
    }
    public None getSwapdirection() {
        return swapDirection;
    }

    public void setSwapdirection(None swapDirection) {
        this.swapDirection = swapDirection;
    }
    public None getSecondpressedcandy() {
        return secondPressedCandy;
    }

    public void setSecondpressedcandy(None secondPressedCandy) {
        this.secondPressedCandy = secondPressedCandy;
    }
    public int getMovesleft() {
        return movesLeft;
    }

    public void setMovesleft(int movesLeft) {
        this.movesLeft = movesLeft;
    }
    public int getMovespergame() {
        return movesPerGame;
    }

    public void setMovespergame(int movesPerGame) {
        this.movesPerGame = movesPerGame;
    }
    public String getCrushtimer() {
        return crushTimer;
    }

    public void setCrushtimer(String crushTimer) {
        this.crushTimer = crushTimer;
    }
    public int getCandyheight() {
        return candyHeight;
    }

    public void setCandyheight(int candyHeight) {
        this.candyHeight = candyHeight;
    }
    public int getGamescore() {
        return gameScore;
    }

    public void setGamescore(int gameScore) {
        this.gameScore = gameScore;
    }
    public int getCrushtimercount() {
        return crushTimerCount;
    }

    public void setCrushtimercount(int crushTimerCount) {
        this.crushTimerCount = crushTimerCount;
    }
    public int getVertical_gap() {
        return VERTICAL_GAP;
    }

    public void setVertical_gap(int VERTICAL_GAP) {
        this.VERTICAL_GAP = VERTICAL_GAP;
    }
    public None getFirstpressedcandy() {
        return firstPressedCandy;
    }

    public void setFirstpressedcandy(None firstPressedCandy) {
        this.firstPressedCandy = firstPressedCandy;
    }
    public int getSize() {
        return SIZE;
    }

    public void setSize(int SIZE) {
        this.SIZE = SIZE;
    }
    public boolean getIsfirstpressed() {
        return isFirstPressed;
    }

    public void setIsfirstpressed(boolean isFirstPressed) {
        this.isFirstPressed = isFirstPressed;
    }
    public String getScorepercandy() {
        return scorePerCandy;
    }

    public void setScorepercandy(String scorePerCandy) {
        this.scorePerCandy = scorePerCandy;
    }
    public int getDelay() {
        return delay;
    }

    public void setDelay(int delay) {
        this.delay = delay;
    }
    public boolean getIsswapback() {
        return isSwapBack;
    }

    public void setIsswapback(boolean isSwapBack) {
        this.isSwapBack = isSwapBack;
    }

    public List<candyCrushPackage_Candy> getCandycrushpackage_candys() {
        return candycrushpackage_candys;
    }

    public void addCandycrushpackage_candy(Candycrushpackage_candy candycrushpackage_candy) {
        this.candycrushpackage_candys.add(candycrushpackage_candy);
    }
    public candyCrushPackage_Game getCandycrushpackage_game() {
        return candycrushpackage_game;
    }

    public void setCandycrushpackage_game(candyCrushPackage_Game candycrushpackage_game) {
        this.candycrushpackage_game = candycrushpackage_game;
    }

}