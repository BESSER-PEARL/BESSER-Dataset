





import java.util.List;
import java.util.ArrayList;

public class candyCrushPackage_Board  {

    private int candyWidth;
    private int moveDistance;
    private int SIZE;
    private int movesLeft;
    private String cascadeTimer;
    private None swapDirection;
    private int crushTimerCount;
    private None secondPressedCandy;
    private String dropTimer;
    private int dropTimerCount;
    private String scorePerCandy;
    private String selfCrushTimer;
    private int delay;
    private int movesPerGame;
    private int BOARD_HEIGHT;
    private String swapTimer;
    private None firstPressedCandy;
    private int gameScore;
    private int baseScorePerCandy;
    private int BOARD_WIDTH;
    private boolean isFirstPressed;
    private None selfCrushCandy;
    private int VERTICAL_GAP;
    private int candyHeight;
    private int HORIZONTAL_GAP;
    private String crushTimer;
    private boolean isSwapBack;
    private int selfCrushTimerCount;
    private int swapTimerCount;





    private List<candyCrushPackage_Candy> candycrushpackage_candys;




    private candyCrushPackage_Game candycrushpackage_game;


    public candyCrushPackage_Board(
        int candyWidth,        int moveDistance,        int SIZE,        int movesLeft,        String cascadeTimer,        None swapDirection,        int crushTimerCount,        None secondPressedCandy,        String dropTimer,        int dropTimerCount,        String scorePerCandy,        String selfCrushTimer,        int delay,        int movesPerGame,        int BOARD_HEIGHT,        String swapTimer,        None firstPressedCandy,        int gameScore,        int baseScorePerCandy,        int BOARD_WIDTH,        boolean isFirstPressed,        None selfCrushCandy,        int VERTICAL_GAP,        int candyHeight,        int HORIZONTAL_GAP,        String crushTimer,        boolean isSwapBack,        int selfCrushTimerCount,        int swapTimerCount    ) {
        this.candyWidth = candyWidth;
        this.moveDistance = moveDistance;
        this.SIZE = SIZE;
        this.movesLeft = movesLeft;
        this.cascadeTimer = cascadeTimer;
        this.swapDirection = swapDirection;
        this.crushTimerCount = crushTimerCount;
        this.secondPressedCandy = secondPressedCandy;
        this.dropTimer = dropTimer;
        this.dropTimerCount = dropTimerCount;
        this.scorePerCandy = scorePerCandy;
        this.selfCrushTimer = selfCrushTimer;
        this.delay = delay;
        this.movesPerGame = movesPerGame;
        this.BOARD_HEIGHT = BOARD_HEIGHT;
        this.swapTimer = swapTimer;
        this.firstPressedCandy = firstPressedCandy;
        this.gameScore = gameScore;
        this.baseScorePerCandy = baseScorePerCandy;
        this.BOARD_WIDTH = BOARD_WIDTH;
        this.isFirstPressed = isFirstPressed;
        this.selfCrushCandy = selfCrushCandy;
        this.VERTICAL_GAP = VERTICAL_GAP;
        this.candyHeight = candyHeight;
        this.HORIZONTAL_GAP = HORIZONTAL_GAP;
        this.crushTimer = crushTimer;
        this.isSwapBack = isSwapBack;
        this.selfCrushTimerCount = selfCrushTimerCount;
        this.swapTimerCount = swapTimerCount;
        this.candycrushpackage_candys = new ArrayList<>();
    }

    public candyCrushPackage_Board(
        int candyWidth,        int moveDistance,        int SIZE,        int movesLeft,        String cascadeTimer,        None swapDirection,        int crushTimerCount,        None secondPressedCandy,        String dropTimer,        int dropTimerCount,        String scorePerCandy,        String selfCrushTimer,        int delay,        int movesPerGame,        int BOARD_HEIGHT,        String swapTimer,        None firstPressedCandy,        int gameScore,        int baseScorePerCandy,        int BOARD_WIDTH,        boolean isFirstPressed,        None selfCrushCandy,        int VERTICAL_GAP,        int candyHeight,        int HORIZONTAL_GAP,        String crushTimer,        boolean isSwapBack,        int selfCrushTimerCount,        int swapTimerCount        ArrayList<candyCrushPackage_Candy> candycrushpackage_candys    ) {
        this.candyWidth = candyWidth;
        this.moveDistance = moveDistance;
        this.SIZE = SIZE;
        this.movesLeft = movesLeft;
        this.cascadeTimer = cascadeTimer;
        this.swapDirection = swapDirection;
        this.crushTimerCount = crushTimerCount;
        this.secondPressedCandy = secondPressedCandy;
        this.dropTimer = dropTimer;
        this.dropTimerCount = dropTimerCount;
        this.scorePerCandy = scorePerCandy;
        this.selfCrushTimer = selfCrushTimer;
        this.delay = delay;
        this.movesPerGame = movesPerGame;
        this.BOARD_HEIGHT = BOARD_HEIGHT;
        this.swapTimer = swapTimer;
        this.firstPressedCandy = firstPressedCandy;
        this.gameScore = gameScore;
        this.baseScorePerCandy = baseScorePerCandy;
        this.BOARD_WIDTH = BOARD_WIDTH;
        this.isFirstPressed = isFirstPressed;
        this.selfCrushCandy = selfCrushCandy;
        this.VERTICAL_GAP = VERTICAL_GAP;
        this.candyHeight = candyHeight;
        this.HORIZONTAL_GAP = HORIZONTAL_GAP;
        this.crushTimer = crushTimer;
        this.isSwapBack = isSwapBack;
        this.selfCrushTimerCount = selfCrushTimerCount;
        this.swapTimerCount = swapTimerCount;
        this.candycrushpackage_candys = candycrushpackage_candys;
    }

    public int getCandywidth() {
        return candyWidth;
    }

    public void setCandywidth(int candyWidth) {
        this.candyWidth = candyWidth;
    }
    public int getMovedistance() {
        return moveDistance;
    }

    public void setMovedistance(int moveDistance) {
        this.moveDistance = moveDistance;
    }
    public int getSize() {
        return SIZE;
    }

    public void setSize(int SIZE) {
        this.SIZE = SIZE;
    }
    public int getMovesleft() {
        return movesLeft;
    }

    public void setMovesleft(int movesLeft) {
        this.movesLeft = movesLeft;
    }
    public String getCascadetimer() {
        return cascadeTimer;
    }

    public void setCascadetimer(String cascadeTimer) {
        this.cascadeTimer = cascadeTimer;
    }
    public None getSwapdirection() {
        return swapDirection;
    }

    public void setSwapdirection(None swapDirection) {
        this.swapDirection = swapDirection;
    }
    public int getCrushtimercount() {
        return crushTimerCount;
    }

    public void setCrushtimercount(int crushTimerCount) {
        this.crushTimerCount = crushTimerCount;
    }
    public None getSecondpressedcandy() {
        return secondPressedCandy;
    }

    public void setSecondpressedcandy(None secondPressedCandy) {
        this.secondPressedCandy = secondPressedCandy;
    }
    public String getDroptimer() {
        return dropTimer;
    }

    public void setDroptimer(String dropTimer) {
        this.dropTimer = dropTimer;
    }
    public int getDroptimercount() {
        return dropTimerCount;
    }

    public void setDroptimercount(int dropTimerCount) {
        this.dropTimerCount = dropTimerCount;
    }
    public String getScorepercandy() {
        return scorePerCandy;
    }

    public void setScorepercandy(String scorePerCandy) {
        this.scorePerCandy = scorePerCandy;
    }
    public String getSelfcrushtimer() {
        return selfCrushTimer;
    }

    public void setSelfcrushtimer(String selfCrushTimer) {
        this.selfCrushTimer = selfCrushTimer;
    }
    public int getDelay() {
        return delay;
    }

    public void setDelay(int delay) {
        this.delay = delay;
    }
    public int getMovespergame() {
        return movesPerGame;
    }

    public void setMovespergame(int movesPerGame) {
        this.movesPerGame = movesPerGame;
    }
    public int getBoard_height() {
        return BOARD_HEIGHT;
    }

    public void setBoard_height(int BOARD_HEIGHT) {
        this.BOARD_HEIGHT = BOARD_HEIGHT;
    }
    public String getSwaptimer() {
        return swapTimer;
    }

    public void setSwaptimer(String swapTimer) {
        this.swapTimer = swapTimer;
    }
    public None getFirstpressedcandy() {
        return firstPressedCandy;
    }

    public void setFirstpressedcandy(None firstPressedCandy) {
        this.firstPressedCandy = firstPressedCandy;
    }
    public int getGamescore() {
        return gameScore;
    }

    public void setGamescore(int gameScore) {
        this.gameScore = gameScore;
    }
    public int getBasescorepercandy() {
        return baseScorePerCandy;
    }

    public void setBasescorepercandy(int baseScorePerCandy) {
        this.baseScorePerCandy = baseScorePerCandy;
    }
    public int getBoard_width() {
        return BOARD_WIDTH;
    }

    public void setBoard_width(int BOARD_WIDTH) {
        this.BOARD_WIDTH = BOARD_WIDTH;
    }
    public boolean getIsfirstpressed() {
        return isFirstPressed;
    }

    public void setIsfirstpressed(boolean isFirstPressed) {
        this.isFirstPressed = isFirstPressed;
    }
    public None getSelfcrushcandy() {
        return selfCrushCandy;
    }

    public void setSelfcrushcandy(None selfCrushCandy) {
        this.selfCrushCandy = selfCrushCandy;
    }
    public int getVertical_gap() {
        return VERTICAL_GAP;
    }

    public void setVertical_gap(int VERTICAL_GAP) {
        this.VERTICAL_GAP = VERTICAL_GAP;
    }
    public int getCandyheight() {
        return candyHeight;
    }

    public void setCandyheight(int candyHeight) {
        this.candyHeight = candyHeight;
    }
    public int getHorizontal_gap() {
        return HORIZONTAL_GAP;
    }

    public void setHorizontal_gap(int HORIZONTAL_GAP) {
        this.HORIZONTAL_GAP = HORIZONTAL_GAP;
    }
    public String getCrushtimer() {
        return crushTimer;
    }

    public void setCrushtimer(String crushTimer) {
        this.crushTimer = crushTimer;
    }
    public boolean getIsswapback() {
        return isSwapBack;
    }

    public void setIsswapback(boolean isSwapBack) {
        this.isSwapBack = isSwapBack;
    }
    public int getSelfcrushtimercount() {
        return selfCrushTimerCount;
    }

    public void setSelfcrushtimercount(int selfCrushTimerCount) {
        this.selfCrushTimerCount = selfCrushTimerCount;
    }
    public int getSwaptimercount() {
        return swapTimerCount;
    }

    public void setSwaptimercount(int swapTimerCount) {
        this.swapTimerCount = swapTimerCount;
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