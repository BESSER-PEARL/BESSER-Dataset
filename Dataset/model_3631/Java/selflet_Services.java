





import java.util.List;
import java.util.ArrayList;

public class selflet_Services  {






    private selflet_SelfletResources selflet_selfletresources;




    private List<selflet_Service> selflet_services;


    public selflet_Services(
    ) {
        this.selflet_services = new ArrayList<>();
    }

    public selflet_Services(
        ArrayList<selflet_Service> selflet_services    ) {
        this.selflet_services = selflet_services;
    }


    public selflet_SelfletResources getSelflet_selfletresources() {
        return selflet_selfletresources;
    }

    public void setSelflet_selfletresources(selflet_SelfletResources selflet_selfletresources) {
        this.selflet_selfletresources = selflet_selfletresources;
    }
    public List<selflet_Service> getSelflet_services() {
        return selflet_services;
    }

    public void addSelflet_service(Selflet_service selflet_service) {
        this.selflet_services.add(selflet_service);
    }

}