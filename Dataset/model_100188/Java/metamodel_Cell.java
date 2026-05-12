





import java.util.List;
import java.util.ArrayList;

public class metamodel_Cell  {

    private String value;





    private metamodel_Column metamodel_column;




    private metamodel_Row metamodel_row;


    public metamodel_Cell(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public metamodel_Column getMetamodel_column() {
        return metamodel_column;
    }

    public void setMetamodel_column(metamodel_Column metamodel_column) {
        this.metamodel_column = metamodel_column;
    }
    public metamodel_Row getMetamodel_row() {
        return metamodel_row;
    }

    public void setMetamodel_row(metamodel_Row metamodel_row) {
        this.metamodel_row = metamodel_row;
    }

}