





import java.util.List;
import java.util.ArrayList;

public class afmmm_AttributedFeatureModel  {






    private afmmm_CrossTreeConstraint afmmm_crosstreeconstraint;




    private List<afmmm_Domain> afmmm_domains;




    private afmmm_AttributedFeatureDiagram afmmm_attributedfeaturediagram;


    public afmmm_AttributedFeatureModel(
    ) {
        this.afmmm_domains = new ArrayList<>();
    }

    public afmmm_AttributedFeatureModel(
        ArrayList<afmmm_Domain> afmmm_domains    ) {
        this.afmmm_domains = afmmm_domains;
    }


    public afmmm_CrossTreeConstraint getAfmmm_crosstreeconstraint() {
        return afmmm_crosstreeconstraint;
    }

    public void setAfmmm_crosstreeconstraint(afmmm_CrossTreeConstraint afmmm_crosstreeconstraint) {
        this.afmmm_crosstreeconstraint = afmmm_crosstreeconstraint;
    }
    public List<afmmm_Domain> getAfmmm_domains() {
        return afmmm_domains;
    }

    public void addAfmmm_domain(Afmmm_domain afmmm_domain) {
        this.afmmm_domains.add(afmmm_domain);
    }
    public afmmm_AttributedFeatureDiagram getAfmmm_attributedfeaturediagram() {
        return afmmm_attributedfeaturediagram;
    }

    public void setAfmmm_attributedfeaturediagram(afmmm_AttributedFeatureDiagram afmmm_attributedfeaturediagram) {
        this.afmmm_attributedfeaturediagram = afmmm_attributedfeaturediagram;
    }

}