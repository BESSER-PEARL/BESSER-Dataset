





import java.util.List;
import java.util.ArrayList;

public class docl_StringLiteralExp extends PrimitiveExp {

    private String segments;



    public docl_StringLiteralExp(
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