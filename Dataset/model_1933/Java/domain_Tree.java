





import java.util.List;
import java.util.ArrayList;

public class domain_Tree extends SourcesPointer, MultiLangLabel, HTMLLayerHolder {

    private String label;





    private List<domain_Column> domain_columns;


    public domain_Tree(
        String label    ) {
        super(
        );
        this.label = label;
        this.domain_columns = new ArrayList<>();
    }

    public domain_Tree(
        String label        ArrayList<domain_Column> domain_columns    ) {
        this.label = label;
        this.domain_columns = domain_columns;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<domain_Column> getDomain_columns() {
        return domain_columns;
    }

    public void addDomain_column(Domain_column domain_column) {
        this.domain_columns.add(domain_column);
    }

}