





import java.util.List;
import java.util.ArrayList;

public class FireworksDisplay  {

    private int NUM_FIREWORKS;
    private String x;
    private int SET_DELAY;
    private String yy;
    private int num;
    private String y;
    private int FIREWORKS_SIZE;
    private String timer;
    private String random;
    private String xx;
    private int FIREWORKS_TIME;
    private int numSets;
    private int startValue;
    private String colors;



    public FireworksDisplay(
        int NUM_FIREWORKS,        String x,        int SET_DELAY,        String yy,        int num,        String y,        int FIREWORKS_SIZE,        String timer,        String random,        String xx,        int FIREWORKS_TIME,        int numSets,        int startValue,        String colors    ) {
        this.NUM_FIREWORKS = NUM_FIREWORKS;
        this.x = x;
        this.SET_DELAY = SET_DELAY;
        this.yy = yy;
        this.num = num;
        this.y = y;
        this.FIREWORKS_SIZE = FIREWORKS_SIZE;
        this.timer = timer;
        this.random = random;
        this.xx = xx;
        this.FIREWORKS_TIME = FIREWORKS_TIME;
        this.numSets = numSets;
        this.startValue = startValue;
        this.colors = colors;
    }


    public int getNum_fireworks() {
        return NUM_FIREWORKS;
    }

    public void setNum_fireworks(int NUM_FIREWORKS) {
        this.NUM_FIREWORKS = NUM_FIREWORKS;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public int getSet_delay() {
        return SET_DELAY;
    }

    public void setSet_delay(int SET_DELAY) {
        this.SET_DELAY = SET_DELAY;
    }
    public String getYy() {
        return yy;
    }

    public void setYy(String yy) {
        this.yy = yy;
    }
    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public int getFireworks_size() {
        return FIREWORKS_SIZE;
    }

    public void setFireworks_size(int FIREWORKS_SIZE) {
        this.FIREWORKS_SIZE = FIREWORKS_SIZE;
    }
    public String getTimer() {
        return timer;
    }

    public void setTimer(String timer) {
        this.timer = timer;
    }
    public String getRandom() {
        return random;
    }

    public void setRandom(String random) {
        this.random = random;
    }
    public String getXx() {
        return xx;
    }

    public void setXx(String xx) {
        this.xx = xx;
    }
    public int getFireworks_time() {
        return FIREWORKS_TIME;
    }

    public void setFireworks_time(int FIREWORKS_TIME) {
        this.FIREWORKS_TIME = FIREWORKS_TIME;
    }
    public int getNumsets() {
        return numSets;
    }

    public void setNumsets(int numSets) {
        this.numSets = numSets;
    }
    public int getStartvalue() {
        return startValue;
    }

    public void setStartvalue(int startValue) {
        this.startValue = startValue;
    }
    public String getColors() {
        return colors;
    }

    public void setColors(String colors) {
        this.colors = colors;
    }


}