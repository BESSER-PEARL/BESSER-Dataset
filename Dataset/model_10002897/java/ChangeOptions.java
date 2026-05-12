





import java.util.List;
import java.util.ArrayList;

public class ChangeOptions  {

    private String easy;
    private String hard;
    private int sounds;
    private boolean exited;
    private int animation;
    private String ok;
    private String winSoundsCheck;
    private String timerCheck;
    private String winAnimationCheck;
    private String drawThree;
    private String drawOne;
    private int drawCount;
    private String medium;
    private int difficulty;
    private int timer;



    public ChangeOptions(
        String easy,        String hard,        int sounds,        boolean exited,        int animation,        String ok,        String winSoundsCheck,        String timerCheck,        String winAnimationCheck,        String drawThree,        String drawOne,        int drawCount,        String medium,        int difficulty,        int timer    ) {
        this.easy = easy;
        this.hard = hard;
        this.sounds = sounds;
        this.exited = exited;
        this.animation = animation;
        this.ok = ok;
        this.winSoundsCheck = winSoundsCheck;
        this.timerCheck = timerCheck;
        this.winAnimationCheck = winAnimationCheck;
        this.drawThree = drawThree;
        this.drawOne = drawOne;
        this.drawCount = drawCount;
        this.medium = medium;
        this.difficulty = difficulty;
        this.timer = timer;
    }


    public String getEasy() {
        return easy;
    }

    public void setEasy(String easy) {
        this.easy = easy;
    }
    public String getHard() {
        return hard;
    }

    public void setHard(String hard) {
        this.hard = hard;
    }
    public int getSounds() {
        return sounds;
    }

    public void setSounds(int sounds) {
        this.sounds = sounds;
    }
    public boolean getExited() {
        return exited;
    }

    public void setExited(boolean exited) {
        this.exited = exited;
    }
    public int getAnimation() {
        return animation;
    }

    public void setAnimation(int animation) {
        this.animation = animation;
    }
    public String getOk() {
        return ok;
    }

    public void setOk(String ok) {
        this.ok = ok;
    }
    public String getWinsoundscheck() {
        return winSoundsCheck;
    }

    public void setWinsoundscheck(String winSoundsCheck) {
        this.winSoundsCheck = winSoundsCheck;
    }
    public String getTimercheck() {
        return timerCheck;
    }

    public void setTimercheck(String timerCheck) {
        this.timerCheck = timerCheck;
    }
    public String getWinanimationcheck() {
        return winAnimationCheck;
    }

    public void setWinanimationcheck(String winAnimationCheck) {
        this.winAnimationCheck = winAnimationCheck;
    }
    public String getDrawthree() {
        return drawThree;
    }

    public void setDrawthree(String drawThree) {
        this.drawThree = drawThree;
    }
    public String getDrawone() {
        return drawOne;
    }

    public void setDrawone(String drawOne) {
        this.drawOne = drawOne;
    }
    public int getDrawcount() {
        return drawCount;
    }

    public void setDrawcount(int drawCount) {
        this.drawCount = drawCount;
    }
    public String getMedium() {
        return medium;
    }

    public void setMedium(String medium) {
        this.medium = medium;
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


}