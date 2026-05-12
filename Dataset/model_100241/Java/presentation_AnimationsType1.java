





import java.util.List;
import java.util.ArrayList;

public class presentation_AnimationsType1  {

    private String group;
    private String presentationAnimationElementsGroup;





    private List<presentation_AnimationGroupType> presentation_animationgrouptypes;




    private List<presentation_EObject> presentation_eobjects;


    public presentation_AnimationsType1(
        String group,        String presentationAnimationElementsGroup    ) {
        this.group = group;
        this.presentationAnimationElementsGroup = presentationAnimationElementsGroup;
        this.presentation_animationgrouptypes = new ArrayList<>();
        this.presentation_eobjects = new ArrayList<>();
    }

    public presentation_AnimationsType1(
        String group,        String presentationAnimationElementsGroup        ArrayList<presentation_AnimationGroupType> presentation_animationgrouptypes,        ArrayList<presentation_EObject> presentation_eobjects    ) {
        this.group = group;
        this.presentationAnimationElementsGroup = presentationAnimationElementsGroup;
        this.presentation_animationgrouptypes = presentation_animationgrouptypes;
        this.presentation_eobjects = presentation_eobjects;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getPresentationanimationelementsgroup() {
        return presentationAnimationElementsGroup;
    }

    public void setPresentationanimationelementsgroup(String presentationAnimationElementsGroup) {
        this.presentationAnimationElementsGroup = presentationAnimationElementsGroup;
    }

    public List<presentation_AnimationGroupType> getPresentation_animationgrouptypes() {
        return presentation_animationgrouptypes;
    }

    public void addPresentation_animationgrouptype(Presentation_animationgrouptype presentation_animationgrouptype) {
        this.presentation_animationgrouptypes.add(presentation_animationgrouptype);
    }
    public List<presentation_EObject> getPresentation_eobjects() {
        return presentation_eobjects;
    }

    public void addPresentation_eobject(Presentation_eobject presentation_eobject) {
        this.presentation_eobjects.add(presentation_eobject);
    }

}