





import java.util.List;
import java.util.ArrayList;

public class FireworksDisplay  {

    private String startValue;
    private String y;
    private String random;
    private String SET_DELAY;
    private String colors;
    private String yy;
    private String x;
    private String numSets;
    private String FIREWORKS_TIME;
    private String FIREWORKS_SIZE;
    private String NUM_FIREWORKS;
    private String xx;
    private String num;
    private String time;



    public FireworksDisplay(
        String startValue,        String y,        String random,        String SET_DELAY,        String colors,        String yy,        String x,        String numSets,        String FIREWORKS_TIME,        String FIREWORKS_SIZE,        String NUM_FIREWORKS,        String xx,        String num,        String time    ) {
        this.startValue = startValue;
        this.y = y;
        this.random = random;
        this.SET_DELAY = SET_DELAY;
        this.colors = colors;
        this.yy = yy;
        this.x = x;
        this.numSets = numSets;
        this.FIREWORKS_TIME = FIREWORKS_TIME;
        this.FIREWORKS_SIZE = FIREWORKS_SIZE;
        this.NUM_FIREWORKS = NUM_FIREWORKS;
        this.xx = xx;
        this.num = num;
        this.time = time;
    }


    public String getStartvalue() {
        return startValue;
    }

    public void setStartvalue(String startValue) {
        this.startValue = startValue;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getRandom() {
        return random;
    }

    public void setRandom(String random) {
        this.random = random;
    }
    public String getSet_delay() {
        return SET_DELAY;
    }

    public void setSet_delay(String SET_DELAY) {
        this.SET_DELAY = SET_DELAY;
    }
    public String getColors() {
        return colors;
    }

    public void setColors(String colors) {
        this.colors = colors;
    }
    public String getYy() {
        return yy;
    }

    public void setYy(String yy) {
        this.yy = yy;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getNumsets() {
        return numSets;
    }

    public void setNumsets(String numSets) {
        this.numSets = numSets;
    }
    public String getFireworks_time() {
        return FIREWORKS_TIME;
    }

    public void setFireworks_time(String FIREWORKS_TIME) {
        this.FIREWORKS_TIME = FIREWORKS_TIME;
    }
    public String getFireworks_size() {
        return FIREWORKS_SIZE;
    }

    public void setFireworks_size(String FIREWORKS_SIZE) {
        this.FIREWORKS_SIZE = FIREWORKS_SIZE;
    }
    public String getNum_fireworks() {
        return NUM_FIREWORKS;
    }

    public void setNum_fireworks(String NUM_FIREWORKS) {
        this.NUM_FIREWORKS = NUM_FIREWORKS;
    }
    public String getXx() {
        return xx;
    }

    public void setXx(String xx) {
        this.xx = xx;
    }
    public String getNum() {
        return num;
    }

    public void setNum(String num) {
        this.num = num;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }


}