





import java.util.List;
import java.util.ArrayList;

public class ChangeOptions  {

    private String drawCount;
    private String difficulty;
    private String hard;
    private String drawOne;
    private String sounds;
    private String winSoundCheck;
    private String timerCheck;
    private String ok;
    private boolean exited;
    private String animation;
    private String drawThree;
    private String timer;
    private String winAnimationCheck;
    private String medium;
    private String easy;



    public ChangeOptions(
        String drawCount,        String difficulty,        String hard,        String drawOne,        String sounds,        String winSoundCheck,        String timerCheck,        String ok,        boolean exited,        String animation,        String drawThree,        String timer,        String winAnimationCheck,        String medium,        String easy    ) {
        this.drawCount = drawCount;
        this.difficulty = difficulty;
        this.hard = hard;
        this.drawOne = drawOne;
        this.sounds = sounds;
        this.winSoundCheck = winSoundCheck;
        this.timerCheck = timerCheck;
        this.ok = ok;
        this.exited = exited;
        this.animation = animation;
        this.drawThree = drawThree;
        this.timer = timer;
        this.winAnimationCheck = winAnimationCheck;
        this.medium = medium;
        this.easy = easy;
    }


    public String getDrawcount() {
        return drawCount;
    }

    public void setDrawcount(String drawCount) {
        this.drawCount = drawCount;
    }
    public String getDifficulty() {
        return difficulty;
    }

    public void setDifficulty(String difficulty) {
        this.difficulty = difficulty;
    }
    public String getHard() {
        return hard;
    }

    public void setHard(String hard) {
        this.hard = hard;
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
    public String getWinsoundcheck() {
        return winSoundCheck;
    }

    public void setWinsoundcheck(String winSoundCheck) {
        this.winSoundCheck = winSoundCheck;
    }
    public String getTimercheck() {
        return timerCheck;
    }

    public void setTimercheck(String timerCheck) {
        this.timerCheck = timerCheck;
    }
    public String getOk() {
        return ok;
    }

    public void setOk(String ok) {
        this.ok = ok;
    }
    public boolean getExited() {
        return exited;
    }

    public void setExited(boolean exited) {
        this.exited = exited;
    }
    public String getAnimation() {
        return animation;
    }

    public void setAnimation(String animation) {
        this.animation = animation;
    }
    public String getDrawthree() {
        return drawThree;
    }

    public void setDrawthree(String drawThree) {
        this.drawThree = drawThree;
    }
    public String getTimer() {
        return timer;
    }

    public void setTimer(String timer) {
        this.timer = timer;
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


}