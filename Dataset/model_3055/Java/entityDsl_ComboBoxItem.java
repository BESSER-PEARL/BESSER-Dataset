





import java.util.List;
import java.util.ArrayList;

public class entityDsl_ComboBoxItem  {

    private String text;





    private entityDsl_ComboBox entitydsl_combobox;


    public entityDsl_ComboBoxItem(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public entityDsl_ComboBox getEntitydsl_combobox() {
        return entitydsl_combobox;
    }

    public void setEntitydsl_combobox(entityDsl_ComboBox entitydsl_combobox) {
        this.entitydsl_combobox = entitydsl_combobox;
    }

}