





import java.util.List;
import java.util.ArrayList;

public class afpText_BII extends structuredField {

    private String ImoName;



    public afpText_BII(
        String ImoName    ) {
        super(
        );
        this.ImoName = ImoName;
    }


    public String getImoname() {
        return ImoName;
    }

    public void setImoname(String ImoName) {
        this.ImoName = ImoName;
    }


}