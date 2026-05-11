





import java.util.List;
import java.util.ArrayList;

public class entityDsl_DataType  {

    private String type;





    private entityDsl_RadioButtonGroup entitydsl_radiobuttongroup;




    private entityDsl_ComboBox entitydsl_combobox;




    private entityDsl_TrackBar entitydsl_trackbar;




    private entityDsl_TextBox entitydsl_textbox;


    public entityDsl_DataType(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public entityDsl_RadioButtonGroup getEntitydsl_radiobuttongroup() {
        return entitydsl_radiobuttongroup;
    }

    public void setEntitydsl_radiobuttongroup(entityDsl_RadioButtonGroup entitydsl_radiobuttongroup) {
        this.entitydsl_radiobuttongroup = entitydsl_radiobuttongroup;
    }
    public entityDsl_ComboBox getEntitydsl_combobox() {
        return entitydsl_combobox;
    }

    public void setEntitydsl_combobox(entityDsl_ComboBox entitydsl_combobox) {
        this.entitydsl_combobox = entitydsl_combobox;
    }
    public entityDsl_TrackBar getEntitydsl_trackbar() {
        return entitydsl_trackbar;
    }

    public void setEntitydsl_trackbar(entityDsl_TrackBar entitydsl_trackbar) {
        this.entitydsl_trackbar = entitydsl_trackbar;
    }
    public entityDsl_TextBox getEntitydsl_textbox() {
        return entitydsl_textbox;
    }

    public void setEntitydsl_textbox(entityDsl_TextBox entitydsl_textbox) {
        this.entitydsl_textbox = entitydsl_textbox;
    }

}