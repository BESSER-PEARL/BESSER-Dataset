





import java.util.List;
import java.util.ArrayList;

public class trnetvisual_NodePattern extends Parameter {

    private float expectedNumberOfDistinctValues;
    private String id;
    private String name;





    private List<trnetvisual_EdgePattern> trnetvisual_edgepatterns;




    private trnetvisual_EdgePattern trnetvisual_edgepattern;




    private List<trnetvisual_Keep> trnetvisual_keeps;




    private trnetvisual_EdgePattern trnetvisual_edgepattern;




    private trnetvisual_Different trnetvisual_different;




    private List<trnetvisual_Same> trnetvisual_sames;




    private trnetvisual_Same trnetvisual_same;




    private trnetvisual_Pattern trnetvisual_pattern;




    private List<trnetvisual_AttributePattern> trnetvisual_attributepatterns;




    private trnetvisual_Pattern trnetvisual_pattern;




    private List<trnetvisual_Different> trnetvisual_differents;




    private trnetvisual_AttributePattern trnetvisual_attributepattern;




    private trnetvisual_Keep trnetvisual_keep;




    private List<trnetvisual_EdgePattern> trnetvisual_edgepatterns;




    private trnetvisual_Different trnetvisual_different;




    private List<trnetvisual_Same> trnetvisual_sames;




    private trnetvisual_Keep trnetvisual_keep;




    private trnetvisual_Same trnetvisual_same;




    private List<trnetvisual_Keep> trnetvisual_keeps;




    private List<trnetvisual_Different> trnetvisual_differents;


    public trnetvisual_NodePattern(
        float expectedNumberOfDistinctValues,        String id,        String name    ) {
        super(
        );
        this.expectedNumberOfDistinctValues = expectedNumberOfDistinctValues;
        this.id = id;
        this.name = name;
        this.trnetvisual_edgepatterns = new ArrayList<>();
        this.trnetvisual_keeps = new ArrayList<>();
        this.trnetvisual_sames = new ArrayList<>();
        this.trnetvisual_attributepatterns = new ArrayList<>();
        this.trnetvisual_differents = new ArrayList<>();
        this.trnetvisual_edgepatterns = new ArrayList<>();
        this.trnetvisual_sames = new ArrayList<>();
        this.trnetvisual_keeps = new ArrayList<>();
        this.trnetvisual_differents = new ArrayList<>();
    }

    public trnetvisual_NodePattern(
        float expectedNumberOfDistinctValues,        String id,        String name        ArrayList<trnetvisual_EdgePattern> trnetvisual_edgepatterns,        ArrayList<trnetvisual_Keep> trnetvisual_keeps,        ArrayList<trnetvisual_Same> trnetvisual_sames,        ArrayList<trnetvisual_AttributePattern> trnetvisual_attributepatterns,        ArrayList<trnetvisual_Different> trnetvisual_differents,        ArrayList<trnetvisual_EdgePattern> trnetvisual_edgepatterns,        ArrayList<trnetvisual_Same> trnetvisual_sames,        ArrayList<trnetvisual_Keep> trnetvisual_keeps,        ArrayList<trnetvisual_Different> trnetvisual_differents    ) {
        this.expectedNumberOfDistinctValues = expectedNumberOfDistinctValues;
        this.id = id;
        this.name = name;
        this.trnetvisual_edgepatterns = trnetvisual_edgepatterns;
        this.trnetvisual_keeps = trnetvisual_keeps;
        this.trnetvisual_sames = trnetvisual_sames;
        this.trnetvisual_attributepatterns = trnetvisual_attributepatterns;
        this.trnetvisual_differents = trnetvisual_differents;
        this.trnetvisual_edgepatterns = trnetvisual_edgepatterns;
        this.trnetvisual_sames = trnetvisual_sames;
        this.trnetvisual_keeps = trnetvisual_keeps;
        this.trnetvisual_differents = trnetvisual_differents;
    }

    public float getExpectednumberofdistinctvalues() {
        return expectedNumberOfDistinctValues;
    }

    public void setExpectednumberofdistinctvalues(float expectedNumberOfDistinctValues) {
        this.expectedNumberOfDistinctValues = expectedNumberOfDistinctValues;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<trnetvisual_EdgePattern> getTrnetvisual_edgepatterns() {
        return trnetvisual_edgepatterns;
    }

    public void addTrnetvisual_edgepattern(Trnetvisual_edgepattern trnetvisual_edgepattern) {
        this.trnetvisual_edgepatterns.add(trnetvisual_edgepattern);
    }
    public trnetvisual_EdgePattern getTrnetvisual_edgepattern() {
        return trnetvisual_edgepattern;
    }

    public void setTrnetvisual_edgepattern(trnetvisual_EdgePattern trnetvisual_edgepattern) {
        this.trnetvisual_edgepattern = trnetvisual_edgepattern;
    }
    public List<trnetvisual_Keep> getTrnetvisual_keeps() {
        return trnetvisual_keeps;
    }

    public void addTrnetvisual_keep(Trnetvisual_keep trnetvisual_keep) {
        this.trnetvisual_keeps.add(trnetvisual_keep);
    }
    public trnetvisual_EdgePattern getTrnetvisual_edgepattern() {
        return trnetvisual_edgepattern;
    }

    public void setTrnetvisual_edgepattern(trnetvisual_EdgePattern trnetvisual_edgepattern) {
        this.trnetvisual_edgepattern = trnetvisual_edgepattern;
    }
    public trnetvisual_Different getTrnetvisual_different() {
        return trnetvisual_different;
    }

    public void setTrnetvisual_different(trnetvisual_Different trnetvisual_different) {
        this.trnetvisual_different = trnetvisual_different;
    }
    public List<trnetvisual_Same> getTrnetvisual_sames() {
        return trnetvisual_sames;
    }

    public void addTrnetvisual_same(Trnetvisual_same trnetvisual_same) {
        this.trnetvisual_sames.add(trnetvisual_same);
    }
    public trnetvisual_Same getTrnetvisual_same() {
        return trnetvisual_same;
    }

    public void setTrnetvisual_same(trnetvisual_Same trnetvisual_same) {
        this.trnetvisual_same = trnetvisual_same;
    }
    public trnetvisual_Pattern getTrnetvisual_pattern() {
        return trnetvisual_pattern;
    }

    public void setTrnetvisual_pattern(trnetvisual_Pattern trnetvisual_pattern) {
        this.trnetvisual_pattern = trnetvisual_pattern;
    }
    public List<trnetvisual_AttributePattern> getTrnetvisual_attributepatterns() {
        return trnetvisual_attributepatterns;
    }

    public void addTrnetvisual_attributepattern(Trnetvisual_attributepattern trnetvisual_attributepattern) {
        this.trnetvisual_attributepatterns.add(trnetvisual_attributepattern);
    }
    public trnetvisual_Pattern getTrnetvisual_pattern() {
        return trnetvisual_pattern;
    }

    public void setTrnetvisual_pattern(trnetvisual_Pattern trnetvisual_pattern) {
        this.trnetvisual_pattern = trnetvisual_pattern;
    }
    public List<trnetvisual_Different> getTrnetvisual_differents() {
        return trnetvisual_differents;
    }

    public void addTrnetvisual_different(Trnetvisual_different trnetvisual_different) {
        this.trnetvisual_differents.add(trnetvisual_different);
    }
    public trnetvisual_AttributePattern getTrnetvisual_attributepattern() {
        return trnetvisual_attributepattern;
    }

    public void setTrnetvisual_attributepattern(trnetvisual_AttributePattern trnetvisual_attributepattern) {
        this.trnetvisual_attributepattern = trnetvisual_attributepattern;
    }
    public trnetvisual_Keep getTrnetvisual_keep() {
        return trnetvisual_keep;
    }

    public void setTrnetvisual_keep(trnetvisual_Keep trnetvisual_keep) {
        this.trnetvisual_keep = trnetvisual_keep;
    }
    public List<trnetvisual_EdgePattern> getTrnetvisual_edgepatterns() {
        return trnetvisual_edgepatterns;
    }

    public void addTrnetvisual_edgepattern(Trnetvisual_edgepattern trnetvisual_edgepattern) {
        this.trnetvisual_edgepatterns.add(trnetvisual_edgepattern);
    }
    public trnetvisual_Different getTrnetvisual_different() {
        return trnetvisual_different;
    }

    public void setTrnetvisual_different(trnetvisual_Different trnetvisual_different) {
        this.trnetvisual_different = trnetvisual_different;
    }
    public List<trnetvisual_Same> getTrnetvisual_sames() {
        return trnetvisual_sames;
    }

    public void addTrnetvisual_same(Trnetvisual_same trnetvisual_same) {
        this.trnetvisual_sames.add(trnetvisual_same);
    }
    public trnetvisual_Keep getTrnetvisual_keep() {
        return trnetvisual_keep;
    }

    public void setTrnetvisual_keep(trnetvisual_Keep trnetvisual_keep) {
        this.trnetvisual_keep = trnetvisual_keep;
    }
    public trnetvisual_Same getTrnetvisual_same() {
        return trnetvisual_same;
    }

    public void setTrnetvisual_same(trnetvisual_Same trnetvisual_same) {
        this.trnetvisual_same = trnetvisual_same;
    }
    public List<trnetvisual_Keep> getTrnetvisual_keeps() {
        return trnetvisual_keeps;
    }

    public void addTrnetvisual_keep(Trnetvisual_keep trnetvisual_keep) {
        this.trnetvisual_keeps.add(trnetvisual_keep);
    }
    public List<trnetvisual_Different> getTrnetvisual_differents() {
        return trnetvisual_differents;
    }

    public void addTrnetvisual_different(Trnetvisual_different trnetvisual_different) {
        this.trnetvisual_differents.add(trnetvisual_different);
    }

}