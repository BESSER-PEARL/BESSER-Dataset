





import java.util.List;
import java.util.ArrayList;

public class myDsl_FM  {






    private List<myDsl_Feature> mydsl_features;




    private List<myDsl_CrossTreeConstraint> mydsl_crosstreeconstraints;




    private List<myDsl_FeatureAttribute> mydsl_featureattributes;




    private List<myDsl_ParentChildConstraint> mydsl_parentchildconstraints;


    public myDsl_FM(
    ) {
        this.mydsl_features = new ArrayList<>();
        this.mydsl_crosstreeconstraints = new ArrayList<>();
        this.mydsl_featureattributes = new ArrayList<>();
        this.mydsl_parentchildconstraints = new ArrayList<>();
    }

    public myDsl_FM(
        ArrayList<myDsl_Feature> mydsl_features,        ArrayList<myDsl_CrossTreeConstraint> mydsl_crosstreeconstraints,        ArrayList<myDsl_FeatureAttribute> mydsl_featureattributes,        ArrayList<myDsl_ParentChildConstraint> mydsl_parentchildconstraints    ) {
        this.mydsl_features = mydsl_features;
        this.mydsl_crosstreeconstraints = mydsl_crosstreeconstraints;
        this.mydsl_featureattributes = mydsl_featureattributes;
        this.mydsl_parentchildconstraints = mydsl_parentchildconstraints;
    }


    public List<myDsl_Feature> getMydsl_features() {
        return mydsl_features;
    }

    public void addMydsl_feature(Mydsl_feature mydsl_feature) {
        this.mydsl_features.add(mydsl_feature);
    }
    public List<myDsl_CrossTreeConstraint> getMydsl_crosstreeconstraints() {
        return mydsl_crosstreeconstraints;
    }

    public void addMydsl_crosstreeconstraint(Mydsl_crosstreeconstraint mydsl_crosstreeconstraint) {
        this.mydsl_crosstreeconstraints.add(mydsl_crosstreeconstraint);
    }
    public List<myDsl_FeatureAttribute> getMydsl_featureattributes() {
        return mydsl_featureattributes;
    }

    public void addMydsl_featureattribute(Mydsl_featureattribute mydsl_featureattribute) {
        this.mydsl_featureattributes.add(mydsl_featureattribute);
    }
    public List<myDsl_ParentChildConstraint> getMydsl_parentchildconstraints() {
        return mydsl_parentchildconstraints;
    }

    public void addMydsl_parentchildconstraint(Mydsl_parentchildconstraint mydsl_parentchildconstraint) {
        this.mydsl_parentchildconstraints.add(mydsl_parentchildconstraint);
    }

}