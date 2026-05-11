





import java.util.List;
import java.util.ArrayList;

public class dft_Named extends GalileoNodeType {

    private String typeName;



    public dft_Named(
        String typeName    ) {
        super(
        );
        this.typeName = typeName;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }


}