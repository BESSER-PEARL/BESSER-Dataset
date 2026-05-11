





import java.util.List;
import java.util.ArrayList;

public class alf_ActiveClassBody  {






    private alf_ActiveClassDefinition alf_activeclassdefinition;




    private alf_BehaviorClause alf_behaviorclause;




    private List<alf_ActiveClassMember> alf_activeclassmembers;




    private alf_ActiveClassDefinitionOrStub alf_activeclassdefinitionorstub;


    public alf_ActiveClassBody(
    ) {
        this.alf_activeclassmembers = new ArrayList<>();
    }

    public alf_ActiveClassBody(
        ArrayList<alf_ActiveClassMember> alf_activeclassmembers    ) {
        this.alf_activeclassmembers = alf_activeclassmembers;
    }


    public alf_ActiveClassDefinition getAlf_activeclassdefinition() {
        return alf_activeclassdefinition;
    }

    public void setAlf_activeclassdefinition(alf_ActiveClassDefinition alf_activeclassdefinition) {
        this.alf_activeclassdefinition = alf_activeclassdefinition;
    }
    public alf_BehaviorClause getAlf_behaviorclause() {
        return alf_behaviorclause;
    }

    public void setAlf_behaviorclause(alf_BehaviorClause alf_behaviorclause) {
        this.alf_behaviorclause = alf_behaviorclause;
    }
    public List<alf_ActiveClassMember> getAlf_activeclassmembers() {
        return alf_activeclassmembers;
    }

    public void addAlf_activeclassmember(Alf_activeclassmember alf_activeclassmember) {
        this.alf_activeclassmembers.add(alf_activeclassmember);
    }
    public alf_ActiveClassDefinitionOrStub getAlf_activeclassdefinitionorstub() {
        return alf_activeclassdefinitionorstub;
    }

    public void setAlf_activeclassdefinitionorstub(alf_ActiveClassDefinitionOrStub alf_activeclassdefinitionorstub) {
        this.alf_activeclassdefinitionorstub = alf_activeclassdefinitionorstub;
    }

}