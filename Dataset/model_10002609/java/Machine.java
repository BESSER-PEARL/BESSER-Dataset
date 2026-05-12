





import java.util.List;
import java.util.ArrayList;

public class Machine  {






    private List<Cache> caches;




    private List<AcceleratorCard> acceleratorcards;


    public Machine(
    ) {
        this.caches = new ArrayList<>();
        this.acceleratorcards = new ArrayList<>();
    }

    public Machine(
        ArrayList<Cache> caches,        ArrayList<AcceleratorCard> acceleratorcards    ) {
        this.caches = caches;
        this.acceleratorcards = acceleratorcards;
    }


    public List<Cache> getCaches() {
        return caches;
    }

    public void addCache(Cache cache) {
        this.caches.add(cache);
    }
    public List<AcceleratorCard> getAcceleratorcards() {
        return acceleratorcards;
    }

    public void addAcceleratorcard(Acceleratorcard acceleratorcard) {
        this.acceleratorcards.add(acceleratorcard);
    }

}