





import java.util.List;
import java.util.ArrayList;

public class Machine  {






    private List<Card> cards;




    private List<Memory_Interface> memory_interfaces;




    private List<Processor> processors;


    public Machine(
    ) {
        this.cards = new ArrayList<>();
        this.memory_interfaces = new ArrayList<>();
        this.processors = new ArrayList<>();
    }

    public Machine(
        ArrayList<Card> cards,        ArrayList<Memory_Interface> memory_interfaces,        ArrayList<Processor> processors    ) {
        this.cards = cards;
        this.memory_interfaces = memory_interfaces;
        this.processors = processors;
    }


    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }
    public List<Memory_Interface> getMemory_interfaces() {
        return memory_interfaces;
    }

    public void addMemory_interface(Memory_interface memory_interface) {
        this.memory_interfaces.add(memory_interface);
    }
    public List<Processor> getProcessors() {
        return processors;
    }

    public void addProcessor(Processor processor) {
        this.processors.add(processor);
    }

}