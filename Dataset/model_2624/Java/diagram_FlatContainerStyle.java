





import java.util.List;
import java.util.ArrayList;

public class diagram_FlatContainerStyle extends ContainerStyle {

    private String backgroundColor;
    private String foregroundColor;
    private String backgroundStyle;



    public diagram_FlatContainerStyle(
        String backgroundColor,        String foregroundColor,        String backgroundStyle    ) {
        super(
        );
        this.backgroundColor = backgroundColor;
        this.foregroundColor = foregroundColor;
        this.backgroundStyle = backgroundStyle;
    }


    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
    }
    public String getForegroundcolor() {
        return foregroundColor;
    }

    public void setForegroundcolor(String foregroundColor) {
        this.foregroundColor = foregroundColor;
    }
    public String getBackgroundstyle() {
        return backgroundStyle;
    }

    public void setBackgroundstyle(String backgroundStyle) {
        this.backgroundStyle = backgroundStyle;
    }


}