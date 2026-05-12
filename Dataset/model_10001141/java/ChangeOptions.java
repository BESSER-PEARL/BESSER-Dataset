





import java.util.List;
import java.util.ArrayList;

public class ChangeOptions  {

    private String animation;
    private String timer;
    private String drawCount;
    private boolean exited;
    private String timerCheck;
    private String winSoundCheck;
    private String hard;
    private String difficulty;
    private String winAnimationCheck;
    private String medium;
    private String easy;
    private String drawOne;
    private String sounds;
    private String ok;
    private String drawThree;



    public ChangeOptions(
        String animation,        String timer,        String drawCount,        boolean exited,        String timerCheck,        String winSoundCheck,        String hard,        String difficulty,        String winAnimationCheck,        String medium,        String easy,        String drawOne,        String sounds,        String ok,        String drawThree    ) {
        this.animation = animation;
        this.timer = timer;
        this.drawCount = drawCount;
        this.exited = exited;
        this.timerCheck = timerCheck;
        this.winSoundCheck = winSoundCheck;
        this.hard = hard;
        this.difficulty = difficulty;
        this.winAnimationCheck = winAnimationCheck;
        this.medium = medium;
        this.easy = easy;
        this.drawOne = drawOne;
        this.sounds = sounds;
        this.ok = ok;
        this.drawThree = drawThree;
    }


    public String getAnimation() {
        return animation;
    }

    public void setAnimation(String animation) {
        this.animation = animation;
    }
    public String getTimer() {
        return timer;
    }

    public void setTimer(String timer) {
        this.timer = timer;
    }
    public String getDrawcount() {
        return drawCount;
    }

    public void setDrawcount(String drawCount) {
        this.drawCount = drawCount;
    }
    public boolean getExited() {
        return exited;
    }

    public void setExited(boolean exited) {
        this.exited = exited;
    }
    public String getTimercheck() {
        return timerCheck;
    }

    public void setTimercheck(String timerCheck) {
        this.timerCheck = timerCheck;
    }
    public String getWinsoundcheck() {
        return winSoundCheck;
    }

    public void setWinsoundcheck(String winSoundCheck) {
        this.winSoundCheck = winSoundCheck;
    }
    public String getHard() {
        return hard;
    }

    public void setHard(String hard) {
        this.hard = hard;
    }
    public String getDifficulty() {
        return difficulty;
    }

    public void setDifficulty(String difficulty) {
        this.difficulty = difficulty;
    }
    public String getWinanimationcheck() {
        return winAnimationCheck;
    }

    public void setWinanimationcheck(String winAnimationCheck) {
        this.winAnimationCheck = winAnimationCheck;
    }
    public String getMedium() {
        return medium;
    }

    public void setMedium(String medium) {
        this.medium = medium;
    }
    public String getEasy() {
        return easy;
    }

    public void setEasy(String easy) {
        this.easy = easy;
    }
    public String getDrawone() {
        return drawOne;
    }

    public void setDrawone(String drawOne) {
        this.drawOne = drawOne;
    }
    public String getSounds() {
        return sounds;
    }

    public void setSounds(String sounds) {
        this.sounds = sounds;
    }
    public String getOk() {
        return ok;
    }

    public void setOk(String ok) {
        this.ok = ok;
    }
    public String getDrawthree() {
        return drawThree;
    }

    public void setDrawthree(String drawThree) {
        this.drawThree = drawThree;
    }


}