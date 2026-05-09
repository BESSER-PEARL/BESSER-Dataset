





import java.util.List;
import java.util.ArrayList;

public class presentation_TableViewer extends AbstractTableViewer {

    private String group4;





    private List<presentation_Table> presentation_tables;


    public presentation_TableViewer(
        String group4    ) {
        super(
        );
        this.group4 = group4;
        this.presentation_tables = new ArrayList<>();
    }

    public presentation_TableViewer(
        String group4        ArrayList<presentation_Table> presentation_tables    ) {
        this.group4 = group4;
        this.presentation_tables = presentation_tables;
    }

    public String getGroup4() {
        return group4;
    }

    public void setGroup4(String group4) {
        this.group4 = group4;
    }

    public List<presentation_Table> getPresentation_tables() {
        return presentation_tables;
    }

    public void addPresentation_table(Presentation_table presentation_table) {
        this.presentation_tables.add(presentation_table);
    }

}