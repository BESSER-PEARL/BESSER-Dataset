





import java.util.List;
import java.util.ArrayList;

public class relationaldatabase_ForeignKey extends NamedElement {

    private String targetLowerBoundary;
    private String targetUpperBoundary;
    private String sourceLowerBoundary;
    private String sourceUpperBoundary;





    private relationaldatabase_Table relationaldatabase_table;




    private List<relationaldatabase_Column> relationaldatabase_columns;




    private relationaldatabase_Table relationaldatabase_table;




    private List<relationaldatabase_Column> relationaldatabase_columns;


    public relationaldatabase_ForeignKey(
        String targetLowerBoundary,        String targetUpperBoundary,        String sourceLowerBoundary,        String sourceUpperBoundary    ) {
        super(
        );
        this.targetLowerBoundary = targetLowerBoundary;
        this.targetUpperBoundary = targetUpperBoundary;
        this.sourceLowerBoundary = sourceLowerBoundary;
        this.sourceUpperBoundary = sourceUpperBoundary;
        this.relationaldatabase_columns = new ArrayList<>();
        this.relationaldatabase_columns = new ArrayList<>();
    }

    public relationaldatabase_ForeignKey(
        String targetLowerBoundary,        String targetUpperBoundary,        String sourceLowerBoundary,        String sourceUpperBoundary        ArrayList<relationaldatabase_Column> relationaldatabase_columns,        ArrayList<relationaldatabase_Column> relationaldatabase_columns    ) {
        this.targetLowerBoundary = targetLowerBoundary;
        this.targetUpperBoundary = targetUpperBoundary;
        this.sourceLowerBoundary = sourceLowerBoundary;
        this.sourceUpperBoundary = sourceUpperBoundary;
        this.relationaldatabase_columns = relationaldatabase_columns;
        this.relationaldatabase_columns = relationaldatabase_columns;
    }

    public String getTargetlowerboundary() {
        return targetLowerBoundary;
    }

    public void setTargetlowerboundary(String targetLowerBoundary) {
        this.targetLowerBoundary = targetLowerBoundary;
    }
    public String getTargetupperboundary() {
        return targetUpperBoundary;
    }

    public void setTargetupperboundary(String targetUpperBoundary) {
        this.targetUpperBoundary = targetUpperBoundary;
    }
    public String getSourcelowerboundary() {
        return sourceLowerBoundary;
    }

    public void setSourcelowerboundary(String sourceLowerBoundary) {
        this.sourceLowerBoundary = sourceLowerBoundary;
    }
    public String getSourceupperboundary() {
        return sourceUpperBoundary;
    }

    public void setSourceupperboundary(String sourceUpperBoundary) {
        this.sourceUpperBoundary = sourceUpperBoundary;
    }

    public relationaldatabase_Table getRelationaldatabase_table() {
        return relationaldatabase_table;
    }

    public void setRelationaldatabase_table(relationaldatabase_Table relationaldatabase_table) {
        this.relationaldatabase_table = relationaldatabase_table;
    }
    public List<relationaldatabase_Column> getRelationaldatabase_columns() {
        return relationaldatabase_columns;
    }

    public void addRelationaldatabase_column(Relationaldatabase_column relationaldatabase_column) {
        this.relationaldatabase_columns.add(relationaldatabase_column);
    }
    public relationaldatabase_Table getRelationaldatabase_table() {
        return relationaldatabase_table;
    }

    public void setRelationaldatabase_table(relationaldatabase_Table relationaldatabase_table) {
        this.relationaldatabase_table = relationaldatabase_table;
    }
    public List<relationaldatabase_Column> getRelationaldatabase_columns() {
        return relationaldatabase_columns;
    }

    public void addRelationaldatabase_column(Relationaldatabase_column relationaldatabase_column) {
        this.relationaldatabase_columns.add(relationaldatabase_column);
    }

}