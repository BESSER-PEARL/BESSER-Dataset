





import java.util.List;
import java.util.ArrayList;

public class iso20022_BusinessArea extends TopLevelCatalogueEntry {

    private String code;



    public iso20022_BusinessArea(
        String code    ) {
        super(
        );
        this.code = code;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }


}