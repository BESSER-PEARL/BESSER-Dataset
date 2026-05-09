





import java.util.List;
import java.util.ArrayList;

public class oCLlite_StringLiteralExp extends PrimitiveExp {

    private String segments;



    public oCLlite_StringLiteralExp(
        String segments    ) {
        super(
        );
        this.segments = segments;
    }


    public String getSegments() {
        return segments;
    }

    public void setSegments(String segments) {
        this.segments = segments;
    }


}