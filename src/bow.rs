use crate::*;

#[derive(Component)]
pub struct Bow {}

impl<'a> System<'a> for Bow {
    type SystemData = (ReadStorage<'a, Bow>, WriteStorage<'a, Position>);

    fn run(&mut self, _data: Self::SystemData) {
        todo!()
    }
}