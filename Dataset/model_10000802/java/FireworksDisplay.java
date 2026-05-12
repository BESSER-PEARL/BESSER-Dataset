





import java.util.List;
import java.util.ArrayList;

public class FireworksDisplay  {

    private String SET_DELAY;
    private String time;
    private String x;
    private String FIREWORKS_SIZE;
    private String FIREWORKS_TIME;
    private String num;
    private String numSets;
    private String xx;
    private String y;
    private String startValue;
    private String yy;
    private String colors;
    private String NUM_FIREWORKS;
    private String random;



    public FireworksDisplay(
        String SET_DELAY,        String time,        String x,        String FIREWORKS_SIZE,        String FIREWORKS_TIME,        String num,        String numSets,        String xx,        String y,        String startValue,        String yy,        String colors,        String NUM_FIREWORKS,        String random    ) {
        this.SET_DELAY = SET_DELAY;
        this.time = time;
        this.x = x;
        this.FIREWORKS_SIZE = FIREWORKS_SIZE;
        this.FIREWORKS_TIME = FIREWORKS_TIME;
        this.num = num;
        this.numSets = numSets;
        this.xx = xx;
        this.y = y;
        this.startValue = startValue;
        this.yy = yy;
        this.colors = colors;
        this.NUM_FIREWORKS = NUM_FIREWORKS;
        this.random = random;
    }


    public String getSet_delay() {
        return SET_DELAY;
    }

    public void setSet_delay(String SET_DELAY) {
        this.SET_DELAY = SET_DELAY;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getFireworks_size() {
        return FIREWORKS_SIZE;
    }

    public void setFireworks_size(String FIREWORKS_SIZE) {
        this.FIREWORKS_SIZE = FIREWORKS_SIZE;
    }
    public String getFireworks_time() {
        return FIREWORKS_TIME;
    }

    public void setFireworks_time(String FIREWORKS_TIME) {
        this.FIREWORKS_TIME = FIREWORKS_TIME;
    }
    public String getNum() {
        return num;
    }

    public void setNum(String num) {
        this.num = num;
    }
    public String getNumsets() {
        return numSets;
    }

    public void setNumsets(String numSets) {
        this.numSets = numSets;
    }
    public String getXx() {
        return xx;
    }

    public void setXx(String xx) {
        this.xx = xx;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getStartvalue() {
        return startValue;
    }

    public void setStartvalue(String startValue) {
        this.startValue = startValue;
    }
    public String getYy() {
        return yy;
    }

    public void setYy(String yy) {
        this.yy = yy;
    }
    public String getColors() {
        return colors;
    }

    public void setColors(String colors) {
        this.colors = colors;
    }
    public String getNum_fireworks() {
        return NUM_FIREWORKS;
    }

    public void setNum_fireworks(String NUM_FIREWORKS) {
        this.NUM_FIREWORKS = NUM_FIREWORKS;
    }
    public String getRandom() {
        return random;
    }

    public void setRandom(String random) {
        this.random = random;
    }


}