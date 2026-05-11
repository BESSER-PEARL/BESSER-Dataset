





import java.util.List;
import java.util.ArrayList;

public class metamodel_Extension_MQPublishing  {

    private String queue;





    private metamodel_EntityObserver metamodel_entityobserver;


    public metamodel_Extension_MQPublishing(
        String queue    ) {
        this.queue = queue;
    }


    public String getQueue() {
        return queue;
    }

    public void setQueue(String queue) {
        this.queue = queue;
    }

    public metamodel_EntityObserver getMetamodel_entityobserver() {
        return metamodel_entityobserver;
    }

    public void setMetamodel_entityobserver(metamodel_EntityObserver metamodel_entityobserver) {
        this.metamodel_entityobserver = metamodel_entityobserver;
    }

}