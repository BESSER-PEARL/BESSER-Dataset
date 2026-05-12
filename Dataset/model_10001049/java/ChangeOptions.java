





import java.util.List;
import java.util.ArrayList;

public class ChangeOptions  {

    private int sounds;
    private int difficulty;
    private int timer;
    private String easy;
    private String winAnimationCheck;
    private String ok;
    private String medium;
    private String drawOne;
    private String drawThree;
    private String winSoundsCheck;
    private boolean exited;
    private int drawCount;
    private String timerCheck;
    private String hard;
    private int animation;



    public ChangeOptions(
        int sounds,        int difficulty,        int timer,        String easy,        String winAnimationCheck,        String ok,        String medium,        String drawOne,        String drawThree,        String winSoundsCheck,        boolean exited,        int drawCount,        String timerCheck,        String hard,        int animation    ) {
        this.sounds = sounds;
        this.difficulty = difficulty;
        this.timer = timer;
        this.easy = easy;
        this.winAnimationCheck = winAnimationCheck;
        this.ok = ok;
        this.medium = medium;
        this.drawOne = drawOne;
        this.drawThree = drawThree;
        this.winSoundsCheck = winSoundsCheck;
        this.exited = exited;
        this.drawCount = drawCount;
        this.timerCheck = timerCheck;
        this.hard = hard;
        this.animation = animation;
    }


    public int getSounds() {
        return sounds;
    }

    public void setSounds(int sounds) {
        this.sounds = sounds;
    }
    public int getDifficulty() {
        return difficulty;
    }

    public void setDifficulty(int difficulty) {
        this.difficulty = difficulty;
    }
    public int getTimer() {
        return timer;
    }

    public void setTimer(int timer) {
        this.timer = timer;
    }
    public String getEasy() {
        return easy;
    }

    public void setEasy(String easy) {
        this.easy = easy;
    }
    public String getWinanimationcheck() {
        return winAnimationCheck;
    }

    public void setWinanimationcheck(String winAnimationCheck) {
        this.winAnimationCheck = winAnimationCheck;
    }
    public String getOk() {
        return ok;
    }

    public void setOk(String ok) {
        this.ok = ok;
    }
    public String getMedium() {
        return medium;
    }

    public void setMedium(String medium) {
        this.medium = medium;
    }
    public String getDrawone() {
        return drawOne;
    }

    public void setDrawone(String drawOne) {
        this.drawOne = drawOne;
    }
    public String getDrawthree() {
        return drawThree;
    }

    public void setDrawthree(String drawThree) {
        this.drawThree = drawThree;
    }
    public String getWinsoundscheck() {
        return winSoundsCheck;
    }

    public void setWinsoundscheck(String winSoundsCheck) {
        this.winSoundsCheck = winSoundsCheck;
    }
    public boolean getExited() {
        return exited;
    }

    public void setExited(boolean exited) {
        this.exited = exited;
    }
    public int getDrawcount() {
        return drawCount;
    }

    public void setDrawcount(int drawCount) {
        this.drawCount = drawCount;
    }
    public String getTimercheck() {
        return timerCheck;
    }

    public void setTimercheck(String timerCheck) {
        this.timerCheck = timerCheck;
    }
    public String getHard() {
        return hard;
    }

    public void setHard(String hard) {
        this.hard = hard;
    }
    public int getAnimation() {
        return animation;
    }

    public void setAnimation(int animation) {
        this.animation = animation;
    }


}