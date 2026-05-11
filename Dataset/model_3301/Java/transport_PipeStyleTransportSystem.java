





import java.util.List;
import java.util.ArrayList;

public class transport_PipeStyleTransportSystem extends TransportSystem {

    private float maxCapacity;



    public transport_PipeStyleTransportSystem(
        float maxCapacity    ) {
        super(
        );
        this.maxCapacity = maxCapacity;
    }


    public float getMaxcapacity() {
        return maxCapacity;
    }

    public void setMaxcapacity(float maxCapacity) {
        this.maxCapacity = maxCapacity;
    }


}