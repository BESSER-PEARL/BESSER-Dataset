





import java.util.List;
import java.util.ArrayList;

public class dcps_DataReaderWriter extends DomainEntity {

    private boolean copyFromTopicQos;



    public dcps_DataReaderWriter(
        boolean copyFromTopicQos    ) {
        super(
        );
        this.copyFromTopicQos = copyFromTopicQos;
    }


    public boolean getCopyfromtopicqos() {
        return copyFromTopicQos;
    }

    public void setCopyfromtopicqos(boolean copyFromTopicQos) {
        this.copyFromTopicQos = copyFromTopicQos;
    }


}