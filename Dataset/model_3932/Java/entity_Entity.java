





import java.util.List;
import java.util.ArrayList;

public class entity_Entity extends Type {






    private List<entity_Member> entity_members;


    public entity_Entity(
    ) {
        super(
        );
        this.entity_members = new ArrayList<>();
    }

    public entity_Entity(
        ArrayList<entity_Member> entity_members    ) {
        this.entity_members = entity_members;
    }


    public List<entity_Member> getEntity_members() {
        return entity_members;
    }

    public void addEntity_member(Entity_member entity_member) {
        this.entity_members.add(entity_member);
    }

}