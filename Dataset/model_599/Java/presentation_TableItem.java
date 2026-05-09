





import java.util.List;
import java.util.ArrayList;

public class presentation_TableItem extends Item {

    private String imageIndent;
    private String texts;
    private String group;
    private String grayed;
    private String checked;





    private List<presentation_Table> presentation_tables;




    private presentation_Table presentation_table;




    private presentation_Table presentation_table;




    private presentation_Cell presentation_cell;


    public presentation_TableItem(
        String imageIndent,        String texts,        String group,        String grayed,        String checked    ) {
        super(
        );
        this.imageIndent = imageIndent;
        this.texts = texts;
        this.group = group;
        this.grayed = grayed;
        this.checked = checked;
        this.presentation_tables = new ArrayList<>();
    }

    public presentation_TableItem(
        String imageIndent,        String texts,        String group,        String grayed,        String checked        ArrayList<presentation_Table> presentation_tables    ) {
        this.imageIndent = imageIndent;
        this.texts = texts;
        this.group = group;
        this.grayed = grayed;
        this.checked = checked;
        this.presentation_tables = presentation_tables;
    }

    public String getImageindent() {
        return imageIndent;
    }

    public void setImageindent(String imageIndent) {
        this.imageIndent = imageIndent;
    }
    public String getTexts() {
        return texts;
    }

    public void setTexts(String texts) {
        this.texts = texts;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getGrayed() {
        return grayed;
    }

    public void setGrayed(String grayed) {
        this.grayed = grayed;
    }
    public String getChecked() {
        return checked;
    }

    public void setChecked(String checked) {
        this.checked = checked;
    }

    public List<presentation_Table> getPresentation_tables() {
        return presentation_tables;
    }

    public void addPresentation_table(Presentation_table presentation_table) {
        this.presentation_tables.add(presentation_table);
    }
    public presentation_Table getPresentation_table() {
        return presentation_table;
    }

    public void setPresentation_table(presentation_Table presentation_table) {
        this.presentation_table = presentation_table;
    }
    public presentation_Table getPresentation_table() {
        return presentation_table;
    }

    public void setPresentation_table(presentation_Table presentation_table) {
        this.presentation_table = presentation_table;
    }
    public presentation_Cell getPresentation_cell() {
        return presentation_cell;
    }

    public void setPresentation_cell(presentation_Cell presentation_cell) {
        this.presentation_cell = presentation_cell;
    }

}