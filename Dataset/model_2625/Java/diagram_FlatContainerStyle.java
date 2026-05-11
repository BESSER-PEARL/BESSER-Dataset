





import java.util.List;
import java.util.ArrayList;

public class diagram_FlatContainerStyle extends ContainerStyle {

    private String foregroundColor;
    private String backgroundStyle;
    private String backgroundColor;



    public diagram_FlatContainerStyle(
        String foregroundColor,        String backgroundStyle,        String backgroundColor    ) {
        super(
        );
        this.foregroundColor = foregroundColor;
        this.backgroundStyle = backgroundStyle;
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
    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
    }


}