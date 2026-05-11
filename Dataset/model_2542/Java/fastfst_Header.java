





import java.util.List;
import java.util.ArrayList;

public class fastfst_Header  {

    private String rows;





    private fastfst_ModelFastfst fastfst_modelfastfst;


    public fastfst_Header(
        String rows    ) {
        this.rows = rows;
    }


    public String getRows() {
        return rows;
    }

    public void setRows(String rows) {
        this.rows = rows;
    }

    public fastfst_ModelFastfst getFastfst_modelfastfst() {
        return fastfst_modelfastfst;
    }

    public void setFastfst_modelfastfst(fastfst_ModelFastfst fastfst_modelfastfst) {
        this.fastfst_modelfastfst = fastfst_modelfastfst;
    }

}