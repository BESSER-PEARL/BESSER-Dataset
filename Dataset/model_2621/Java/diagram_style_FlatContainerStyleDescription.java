





import java.util.List;
import java.util.ArrayList;

public class diagram_style_FlatContainerStyleDescription extends style_ContainerStyleDescription, style_SizeComputationContainerStyleDescription {

    private String backgroundStyle;



    public diagram_style_FlatContainerStyleDescription(
        String backgroundStyle    ) {
        super(
        );
        this.backgroundStyle = backgroundStyle;
    }


    public String getBackgroundstyle() {
        return backgroundStyle;
    }

    public void setBackgroundstyle(String backgroundStyle) {
        this.backgroundStyle = backgroundStyle;
    }


}