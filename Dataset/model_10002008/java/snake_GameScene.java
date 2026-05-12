





import java.util.List;
import java.util.ArrayList;

public class snake_GameScene  {

    private None bg;
    private int B_HEIGHT;
    private int ALL_DOTS;
    private int level;
    private int B_WIDTH;
    private int DOT_SIZE;
    private boolean leftDirection;
    private int serialVersionUID;
    private int apple_y;
    private int myScore;
    private boolean downDirection;
    private int RAND_POS;
    private int DELAY;
    private None timer;
    private String y;
    private None bodySegment;
    private None head;
    private int bodyLength;
    private boolean rightDirection;
    private int apple_x;
    private None apple;
    private String x;
    private boolean upDirection;
    private boolean inGame;



    public snake_GameScene(
        None bg,        int B_HEIGHT,        int ALL_DOTS,        int level,        int B_WIDTH,        int DOT_SIZE,        boolean leftDirection,        int serialVersionUID,        int apple_y,        int myScore,        boolean downDirection,        int RAND_POS,        int DELAY,        None timer,        String y,        None bodySegment,        None head,        int bodyLength,        boolean rightDirection,        int apple_x,        None apple,        String x,        boolean upDirection,        boolean inGame    ) {
        this.bg = bg;
        this.B_HEIGHT = B_HEIGHT;
        this.ALL_DOTS = ALL_DOTS;
        this.level = level;
        this.B_WIDTH = B_WIDTH;
        this.DOT_SIZE = DOT_SIZE;
        this.leftDirection = leftDirection;
        this.serialVersionUID = serialVersionUID;
        this.apple_y = apple_y;
        this.myScore = myScore;
        this.downDirection = downDirection;
        this.RAND_POS = RAND_POS;
        this.DELAY = DELAY;
        this.timer = timer;
        this.y = y;
        this.bodySegment = bodySegment;
        this.head = head;
        this.bodyLength = bodyLength;
        this.rightDirection = rightDirection;
        this.apple_x = apple_x;
        this.apple = apple;
        this.x = x;
        this.upDirection = upDirection;
        this.inGame = inGame;
    }


    public None getBg() {
        return bg;
    }

    public void setBg(None bg) {
        this.bg = bg;
    }
    public int getB_height() {
        return B_HEIGHT;
    }

    public void setB_height(int B_HEIGHT) {
        this.B_HEIGHT = B_HEIGHT;
    }
    public int getAll_dots() {
        return ALL_DOTS;
    }

    public void setAll_dots(int ALL_DOTS) {
        this.ALL_DOTS = ALL_DOTS;
    }
    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }
    public int getB_width() {
        return B_WIDTH;
    }

    public void setB_width(int B_WIDTH) {
        this.B_WIDTH = B_WIDTH;
    }
    public int getDot_size() {
        return DOT_SIZE;
    }

    public void setDot_size(int DOT_SIZE) {
        this.DOT_SIZE = DOT_SIZE;
    }
    public boolean getLeftdirection() {
        return leftDirection;
    }

    public void setLeftdirection(boolean leftDirection) {
        this.leftDirection = leftDirection;
    }
    public int getSerialversionuid() {
        return serialVersionUID;
    }

    public void setSerialversionuid(int serialVersionUID) {
        this.serialVersionUID = serialVersionUID;
    }
    public int getApple_y() {
        return apple_y;
    }

    public void setApple_y(int apple_y) {
        this.apple_y = apple_y;
    }
    public int getMyscore() {
        return myScore;
    }

    public void setMyscore(int myScore) {
        this.myScore = myScore;
    }
    public boolean getDowndirection() {
        return downDirection;
    }

    public void setDowndirection(boolean downDirection) {
        this.downDirection = downDirection;
    }
    public int getRand_pos() {
        return RAND_POS;
    }

    public void setRand_pos(int RAND_POS) {
        this.RAND_POS = RAND_POS;
    }
    public int getDelay() {
        return DELAY;
    }

    public void setDelay(int DELAY) {
        this.DELAY = DELAY;
    }
    public None getTimer() {
        return timer;
    }

    public void setTimer(None timer) {
        this.timer = timer;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public None getBodysegment() {
        return bodySegment;
    }

    public void setBodysegment(None bodySegment) {
        this.bodySegment = bodySegment;
    }
    public None getHead() {
        return head;
    }

    public void setHead(None head) {
        this.head = head;
    }
    public int getBodylength() {
        return bodyLength;
    }

    public void setBodylength(int bodyLength) {
        this.bodyLength = bodyLength;
    }
    public boolean getRightdirection() {
        return rightDirection;
    }

    public void setRightdirection(boolean rightDirection) {
        this.rightDirection = rightDirection;
    }
    public int getApple_x() {
        return apple_x;
    }

    public void setApple_x(int apple_x) {
        this.apple_x = apple_x;
    }
    public None getApple() {
        return apple;
    }

    public void setApple(None apple) {
        this.apple = apple;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public boolean getUpdirection() {
        return upDirection;
    }

    public void setUpdirection(boolean upDirection) {
        this.upDirection = upDirection;
    }
    public boolean getIngame() {
        return inGame;
    }

    public void setIngame(boolean inGame) {
        this.inGame = inGame;
    }


}