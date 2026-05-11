





import java.util.List;
import java.util.ArrayList;

public class moba_MobaCache extends MobaApplicationFeature {

    private String cacheStrategyString;
    private int cacheIntervalInt;
    private String name;
    private String cacheTypeString;





    private moba_MobaApplication moba_mobaapplication;


    public moba_MobaCache(
        String cacheStrategyString,        int cacheIntervalInt,        String name,        String cacheTypeString    ) {
        super(
        );
        this.cacheStrategyString = cacheStrategyString;
        this.cacheIntervalInt = cacheIntervalInt;
        this.name = name;
        this.cacheTypeString = cacheTypeString;
    }


    public String getCachestrategystring() {
        return cacheStrategyString;
    }

    public void setCachestrategystring(String cacheStrategyString) {
        this.cacheStrategyString = cacheStrategyString;
    }
    public int getCacheintervalint() {
        return cacheIntervalInt;
    }

    public void setCacheintervalint(int cacheIntervalInt) {
        this.cacheIntervalInt = cacheIntervalInt;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCachetypestring() {
        return cacheTypeString;
    }

    public void setCachetypestring(String cacheTypeString) {
        this.cacheTypeString = cacheTypeString;
    }

    public moba_MobaApplication getMoba_mobaapplication() {
        return moba_mobaapplication;
    }

    public void setMoba_mobaapplication(moba_MobaApplication moba_mobaapplication) {
        this.moba_mobaapplication = moba_mobaapplication;
    }

}