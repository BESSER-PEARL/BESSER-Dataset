





import java.util.List;
import java.util.ArrayList;

public class selflet_TypeKnowledge  {






    private selflet_SelfletProperties selflet_selfletproperties;




    private List<selflet_SelfLetProperty> selflet_selfletpropertys;


    public selflet_TypeKnowledge(
    ) {
        this.selflet_selfletpropertys = new ArrayList<>();
    }

    public selflet_TypeKnowledge(
        ArrayList<selflet_SelfLetProperty> selflet_selfletpropertys    ) {
        this.selflet_selfletpropertys = selflet_selfletpropertys;
    }


    public selflet_SelfletProperties getSelflet_selfletproperties() {
        return selflet_selfletproperties;
    }

    public void setSelflet_selfletproperties(selflet_SelfletProperties selflet_selfletproperties) {
        this.selflet_selfletproperties = selflet_selfletproperties;
    }
    public List<selflet_SelfLetProperty> getSelflet_selfletpropertys() {
        return selflet_selfletpropertys;
    }

    public void addSelflet_selfletproperty(Selflet_selfletproperty selflet_selfletproperty) {
        this.selflet_selfletpropertys.add(selflet_selfletproperty);
    }

}