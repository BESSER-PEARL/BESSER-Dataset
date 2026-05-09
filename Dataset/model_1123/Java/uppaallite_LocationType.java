





import java.util.List;
import java.util.ArrayList;

public class uppaallite_LocationType  {

    private String invariant;
    private String cost;
    private String id;
    private int x;
    private boolean urgent;
    private boolean committed;
    private boolean initial;
    private String name;
    private int y;



    public uppaallite_LocationType(
        String invariant,        String cost,        String id,        int x,        boolean urgent,        boolean committed,        boolean initial,        String name,        int y    ) {
        this.invariant = invariant;
        this.cost = cost;
        this.id = id;
        this.x = x;
        this.urgent = urgent;
        this.committed = committed;
        this.initial = initial;
        this.name = name;
        this.y = y;
    }


    public String getInvariant() {
        return invariant;
    }

    public void setInvariant(String invariant) {
        this.invariant = invariant;
    }
    public String getCost() {
        return cost;
    }

    public void setCost(String cost) {
        this.cost = cost;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public boolean getUrgent() {
        return urgent;
    }

    public void setUrgent(boolean urgent) {
        this.urgent = urgent;
    }
    public boolean getCommitted() {
        return committed;
    }

    public void setCommitted(boolean committed) {
        this.committed = committed;
    }
    public boolean getInitial() {
        return initial;
    }

    public void setInitial(boolean initial) {
        this.initial = initial;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }


}