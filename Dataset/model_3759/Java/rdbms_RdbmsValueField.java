





import java.util.List;
import java.util.ArrayList;

public class rdbms_RdbmsValueField extends RdbmsField {

    private boolean technical;



    public rdbms_RdbmsValueField(
        boolean technical    ) {
        super(
        );
        this.technical = technical;
    }


    public boolean getTechnical() {
        return technical;
    }

    public void setTechnical(boolean technical) {
        this.technical = technical;
    }


}