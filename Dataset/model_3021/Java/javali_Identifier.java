





import java.util.List;
import java.util.ArrayList;

public class javali_Identifier  {

    private String id;





    private javali_Type javali_type;


    public javali_Identifier(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public javali_Type getJavali_type() {
        return javali_type;
    }

    public void setJavali_type(javali_Type javali_type) {
        this.javali_type = javali_type;
    }

}