





import java.util.List;
import java.util.ArrayList;

public class graphgenerators_MigrationEdgeGraphGenerator extends GraphGenerator {

    private String population;
    private float migrationRate;
    private String location;



    public graphgenerators_MigrationEdgeGraphGenerator(
        String population,        float migrationRate,        String location    ) {
        super(
        );
        this.population = population;
        this.migrationRate = migrationRate;
        this.location = location;
    }


    public String getPopulation() {
        return population;
    }

    public void setPopulation(String population) {
        this.population = population;
    }
    public float getMigrationrate() {
        return migrationRate;
    }

    public void setMigrationrate(float migrationRate) {
        this.migrationRate = migrationRate;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}