





import java.util.List;
import java.util.ArrayList;

public class diagram_FlatContainerStyle extends ContainerStyle {

    private String foregroundColor;
    private String backgroundColor;
    private String backgroundStyle;



    public diagram_FlatContainerStyle(
        String foregroundColor,        String backgroundColor,        String backgroundStyle    ) {
        super(
        );
        this.foregroundColor = foregroundColor;
        this.backgroundColor = backgroundColor;
        this.backgroundStyle = backgroundStyle;
    }


    public String getForegroundcolor() {
        return foregroundColor;
    }

    public void setForegroundcolor(String foregroundColor) {
        this.foregroundColor = foregroundColor;
    }
    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
    }
    public String getBackgroundstyle() {
        return backgroundStyle;
    }

    public void setBackgroundstyle(String backgroundStyle) {
        this.backgroundStyle = backgroundStyle;
    }


}