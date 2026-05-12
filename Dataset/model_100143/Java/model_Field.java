





import java.util.List;
import java.util.ArrayList;

public class model_Field extends SeparatedElement, IColumn {

    private String length;
    private String position;
    private String type;



    public model_Field(
        String length,        String position,        String type    ) {
        super(
        );
        this.length = length;
        this.position = position;
        this.type = type;
    }


    public String getLength() {
        return length;
    }

    public void setLength(String length) {
        this.length = length;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}