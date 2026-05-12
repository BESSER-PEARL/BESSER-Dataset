





import java.util.List;
import java.util.ArrayList;

public class presentation_SettingsType  {

    private String transitionOnClick;
    private String fullScreen;
    private String endless;
    private String showLogo;
    private String stayOnTop;
    private String startWithNavigator;
    private String forceManual;
    private String mouseAsPen;
    private String mouseVisible;
    private String showEndOfPresentationSlide;
    private String animations;
    private String show1;
    private String pause;
    private String startPage;



    public presentation_SettingsType(
        String transitionOnClick,        String fullScreen,        String endless,        String showLogo,        String stayOnTop,        String startWithNavigator,        String forceManual,        String mouseAsPen,        String mouseVisible,        String showEndOfPresentationSlide,        String animations,        String show1,        String pause,        String startPage    ) {
        this.transitionOnClick = transitionOnClick;
        this.fullScreen = fullScreen;
        this.endless = endless;
        this.showLogo = showLogo;
        this.stayOnTop = stayOnTop;
        this.startWithNavigator = startWithNavigator;
        this.forceManual = forceManual;
        this.mouseAsPen = mouseAsPen;
        this.mouseVisible = mouseVisible;
        this.showEndOfPresentationSlide = showEndOfPresentationSlide;
        this.animations = animations;
        this.show1 = show1;
        this.pause = pause;
        this.startPage = startPage;
    }


    public String getTransitiononclick() {
        return transitionOnClick;
    }

    public void setTransitiononclick(String transitionOnClick) {
        this.transitionOnClick = transitionOnClick;
    }
    public String getFullscreen() {
        return fullScreen;
    }

    public void setFullscreen(String fullScreen) {
        this.fullScreen = fullScreen;
    }
    public String getEndless() {
        return endless;
    }

    public void setEndless(String endless) {
        this.endless = endless;
    }
    public String getShowlogo() {
        return showLogo;
    }

    public void setShowlogo(String showLogo) {
        this.showLogo = showLogo;
    }
    public String getStayontop() {
        return stayOnTop;
    }

    public void setStayontop(String stayOnTop) {
        this.stayOnTop = stayOnTop;
    }
    public String getStartwithnavigator() {
        return startWithNavigator;
    }

    public void setStartwithnavigator(String startWithNavigator) {
        this.startWithNavigator = startWithNavigator;
    }
    public String getForcemanual() {
        return forceManual;
    }

    public void setForcemanual(String forceManual) {
        this.forceManual = forceManual;
    }
    public String getMouseaspen() {
        return mouseAsPen;
    }

    public void setMouseaspen(String mouseAsPen) {
        this.mouseAsPen = mouseAsPen;
    }
    public String getMousevisible() {
        return mouseVisible;
    }

    public void setMousevisible(String mouseVisible) {
        this.mouseVisible = mouseVisible;
    }
    public String getShowendofpresentationslide() {
        return showEndOfPresentationSlide;
    }

    public void setShowendofpresentationslide(String showEndOfPresentationSlide) {
        this.showEndOfPresentationSlide = showEndOfPresentationSlide;
    }
    public String getAnimations() {
        return animations;
    }

    public void setAnimations(String animations) {
        this.animations = animations;
    }
    public String getShow1() {
        return show1;
    }

    public void setShow1(String show1) {
        this.show1 = show1;
    }
    public String getPause() {
        return pause;
    }

    public void setPause(String pause) {
        this.pause = pause;
    }
    public String getStartpage() {
        return startPage;
    }

    public void setStartpage(String startPage) {
        this.startPage = startPage;
    }


}