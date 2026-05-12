





import java.util.List;
import java.util.ArrayList;

public class Tenant  {

    private String name;
    private String id;





    private List<AbstractEntity> abstractentitys;




    private List<AbstractEntity> abstractentitys;


    public Tenant(
        String name,        String id    ) {
        this.name = name;
        this.id = id;
        this.abstractentitys = new ArrayList<>();
        this.abstractentitys = new ArrayList<>();
    }

    public Tenant(
        String name,        String id        ArrayList<AbstractEntity> abstractentitys,        ArrayList<AbstractEntity> abstractentitys    ) {
        this.name = name;
        this.id = id;
        this.abstractentitys = abstractentitys;
        this.abstractentitys = abstractentitys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<AbstractEntity> getAbstractentitys() {
        return abstractentitys;
    }

    public void addAbstractentity(Abstractentity abstractentity) {
        this.abstractentitys.add(abstractentity);
    }
    public List<AbstractEntity> getAbstractentitys() {
        return abstractentitys;
    }

    public void addAbstractentity(Abstractentity abstractentity) {
        this.abstractentitys.add(abstractentity);
    }

}